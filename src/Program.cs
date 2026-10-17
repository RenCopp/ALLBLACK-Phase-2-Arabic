using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.IO.Compression;
using System.Reflection;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Win32;

namespace AllblackArabicInstaller
{
    internal static class Program
    {
        [STAThread]
        private static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new InstallerForm());
        }
    }

    internal sealed class InstallerForm : Form
    {
        private const string GameExe = "ALLBLACKPhase2.exe";
        private readonly TextBox pathBox;
        private readonly Label statusLabel;
        private readonly ProgressBar progress;
        private readonly Button installButton;
        private readonly Button uninstallButton;
        private readonly Button browseButton;

        public InstallerForm()
        {
            Text = "ALLBLACK Phase 2 — Arabic Localization";
            ClientSize = new Size(760, 485);
            MinimumSize = new Size(776, 524);
            StartPosition = FormStartPosition.CenterScreen;
            BackColor = Color.FromArgb(12, 17, 27);
            ForeColor = Color.WhiteSmoke;
            Font = new Font("Segoe UI", 10F);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;

            Panel header = new Panel { Dock = DockStyle.Top, Height = 118, BackColor = Color.FromArgb(18, 27, 43) };
            Controls.Add(header);

            Label mark = new Label {
                Text = "A", AutoSize = false, Size = new Size(66, 66), Location = new Point(35, 25),
                TextAlign = ContentAlignment.MiddleCenter, Font = new Font("Segoe UI", 29F, FontStyle.Bold),
                ForeColor = Color.White, BackColor = Color.FromArgb(220, 35, 45)
            };
            header.Controls.Add(mark);

            Label title = new Label {
                Text = "ALLBLACK Phase 2", AutoSize = true, Location = new Point(120, 22),
                Font = new Font("Segoe UI Semibold", 22F), ForeColor = Color.White
            };
            header.Controls.Add(title);

            Label subtitle = new Label {
                Text = "التعريب العربي  •  Arabic Localization", AutoSize = true, Location = new Point(123, 66),
                Font = new Font("Segoe UI", 12F), ForeColor = Color.FromArgb(187, 201, 222),
                RightToLeft = RightToLeft.Yes
            };
            header.Controls.Add(subtitle);

            Label intro = new Label {
                Text = "تثبيت الترجمة العربية، خط Noto Sans Arabic، ودعم العرض من اليمين إلى اليسار.",
                AutoSize = false, Size = new Size(690, 30), Location = new Point(35, 140),
                TextAlign = ContentAlignment.MiddleRight, RightToLeft = RightToLeft.Yes,
                ForeColor = Color.FromArgb(220, 225, 235)
            };
            Controls.Add(intro);

            Label pathLabel = new Label {
                Text = "مجلد اللعبة  /  Game folder", AutoSize = true, Location = new Point(35, 190),
                RightToLeft = RightToLeft.Yes, Font = new Font("Segoe UI Semibold", 10F)
            };
            Controls.Add(pathLabel);

            pathBox = new TextBox {
                Location = new Point(35, 218), Size = new Size(584, 28), BackColor = Color.FromArgb(28, 38, 55),
                ForeColor = Color.White, BorderStyle = BorderStyle.FixedSingle
            };
            Controls.Add(pathBox);

            browseButton = MakeButton("استعراض…", new Point(632, 216), new Size(93, 32), Color.FromArgb(65, 78, 99));
            browseButton.Click += Browse;
            Controls.Add(browseButton);

            Label note = new Label {
                Text = "سيتم إنشاء نسخة احتياطية تلقائيًا قبل استبدال أي ملفات موجودة.",
                AutoSize = false, Size = new Size(690, 26), Location = new Point(35, 260),
                TextAlign = ContentAlignment.MiddleRight, RightToLeft = RightToLeft.Yes,
                ForeColor = Color.FromArgb(148, 164, 187)
            };
            Controls.Add(note);

            progress = new ProgressBar { Location = new Point(35, 303), Size = new Size(690, 16), Style = ProgressBarStyle.Continuous };
            Controls.Add(progress);

            statusLabel = new Label {
                Text = "جاهز للتثبيت", AutoSize = false, Size = new Size(690, 48), Location = new Point(35, 329),
                TextAlign = ContentAlignment.TopRight, RightToLeft = RightToLeft.Yes,
                ForeColor = Color.FromArgb(187, 201, 222)
            };
            Controls.Add(statusLabel);

            installButton = MakeButton("تثبيت التعريب", new Point(481, 398), new Size(244, 48), Color.FromArgb(198, 31, 42));
            installButton.Font = new Font("Segoe UI Semibold", 11F);
            installButton.Click += async delegate { await InstallAsync(); };
            Controls.Add(installButton);

            uninstallButton = MakeButton("إزالة التعريب", new Point(225, 398), new Size(244, 48), Color.FromArgb(54, 66, 84));
            uninstallButton.Font = new Font("Segoe UI Semibold", 11F);
            uninstallButton.Click += async delegate { await UninstallAsync(); };
            Controls.Add(uninstallButton);

            Button closeButton = MakeButton("إغلاق", new Point(35, 398), new Size(150, 48), Color.FromArgb(38, 47, 62));
            closeButton.Click += delegate { Close(); };
            Controls.Add(closeButton);

            pathBox.Text = FindGameDirectory() ?? "";
            UpdatePathState();
            pathBox.TextChanged += delegate { UpdatePathState(); };
        }

        private static Button MakeButton(string text, Point location, Size size, Color color)
        {
            Button button = new Button {
                Text = text, Location = location, Size = size, FlatStyle = FlatStyle.Flat,
                BackColor = color, ForeColor = Color.White, Cursor = Cursors.Hand,
                RightToLeft = RightToLeft.Yes
            };
            button.FlatAppearance.BorderSize = 0;
            button.FlatAppearance.MouseOverBackColor = ControlPaint.Light(color, 0.12F);
            return button;
        }

        private void Browse(object sender, EventArgs e)
        {
            using (FolderBrowserDialog dialog = new FolderBrowserDialog())
            {
                dialog.Description = "اختر مجلد ALLBLACK Phase 2 الذي يحتوي على ALLBLACKPhase2.exe";
                dialog.SelectedPath = Directory.Exists(pathBox.Text) ? pathBox.Text : "";
                if (dialog.ShowDialog(this) == DialogResult.OK)
                    pathBox.Text = dialog.SelectedPath;
            }
        }

        private bool IsValidGameDirectory(string path)
        {
            return Directory.Exists(path) && File.Exists(Path.Combine(path, GameExe)) && Directory.Exists(Path.Combine(path, "game"));
        }

        private void UpdatePathState()
        {
            bool valid = IsValidGameDirectory(pathBox.Text.Trim());
            installButton.Enabled = valid;
            uninstallButton.Enabled = valid;
            statusLabel.Text = valid ? "تم العثور على اللعبة. يمكنك تثبيت التعريب الآن." : "اختر مجلد اللعبة الصحيح الذي يحتوي على " + GameExe;
            statusLabel.ForeColor = valid ? Color.FromArgb(128, 214, 154) : Color.FromArgb(240, 178, 91);
        }

        private async Task InstallAsync()
        {
            string root = Path.GetFullPath(pathBox.Text.Trim());
            if (!IsValidGameDirectory(root)) { UpdatePathState(); return; }
            SetBusy(true, "جارٍ تثبيت التعريب…");
            try
            {
                await Task.Run(delegate { Install(root); });
                progress.Value = 100;
                statusLabel.ForeColor = Color.FromArgb(128, 214, 154);
                statusLabel.Text = "اكتمل التثبيت بنجاح. شغّل اللعبة واستمتع بالتعريب العربي.";
                MessageBox.Show(this, "اكتمل تثبيت التعريب العربي بنجاح.", "تم التثبيت", MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1, MessageBoxOptions.RtlReading);
            }
            catch (Exception ex)
            {
                statusLabel.ForeColor = Color.FromArgb(239, 107, 112);
                statusLabel.Text = "فشل التثبيت: " + ex.Message;
                MessageBox.Show(this, ex.Message, "تعذر التثبيت", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally { SetBusy(false, null); }
        }

        private void Install(string root)
        {
            string stamp = DateTime.Now.ToString("yyyyMMdd-HHmmss");
            string backup = Path.Combine(root, "ArabicLocalizationBackup", stamp);
            string[] existing = {
                Path.Combine(root, "game", "tl", "arabic"),
                Path.Combine(root, "game", "zz_arabic_support.rpy"),
                Path.Combine(root, "game", "zz_arabic_support.rpyc"),
                Path.Combine(root, "game", "NotoSansArabic.ttf")
            };
            bool madeBackup = false;
            foreach (string item in existing)
            {
                if (Directory.Exists(item))
                {
                    CopyDirectory(item, Path.Combine(backup, RelativeTo(root, item)));
                    madeBackup = true;
                }
                else if (File.Exists(item))
                {
                    string destination = Path.Combine(backup, RelativeTo(root, item));
                    Directory.CreateDirectory(Path.GetDirectoryName(destination));
                    File.Copy(item, destination, true);
                    madeBackup = true;
                }
            }
            if (!madeBackup && Directory.Exists(backup)) Directory.Delete(backup, true);

            Stream payload = Assembly.GetExecutingAssembly().GetManifestResourceStream("Payload.Zip");
            if (payload == null) throw new InvalidOperationException("Installer payload is missing.");
            using (payload)
            using (ZipArchive archive = new ZipArchive(payload, ZipArchiveMode.Read))
            {
                int total = Math.Max(archive.Entries.Count, 1);
                int index = 0;
                foreach (ZipArchiveEntry entry in archive.Entries)
                {
                    string destination = Path.GetFullPath(Path.Combine(root, entry.FullName.Replace('/', Path.DirectorySeparatorChar)));
                    if (!destination.StartsWith(root + Path.DirectorySeparatorChar, StringComparison.OrdinalIgnoreCase))
                        throw new InvalidDataException("Invalid path in installer payload.");
                    if (String.IsNullOrEmpty(entry.Name)) Directory.CreateDirectory(destination);
                    else
                    {
                        Directory.CreateDirectory(Path.GetDirectoryName(destination));
                        entry.ExtractToFile(destination, true);
                    }
                    index++;
                    int value = index * 100 / total;
                    BeginInvoke((Action)delegate { progress.Value = Math.Max(0, Math.Min(100, value)); });
                }
            }
        }

        private async Task UninstallAsync()
        {
            string root = Path.GetFullPath(pathBox.Text.Trim());
            if (!IsValidGameDirectory(root)) { UpdatePathState(); return; }
            DialogResult answer = MessageBox.Show(this, "هل تريد إزالة ملفات التعريب العربي؟\nلن تُحذف ملفات اللعبة الأصلية.", "إزالة التعريب", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button2, MessageBoxOptions.RtlReading);
            if (answer != DialogResult.Yes) return;
            SetBusy(true, "جارٍ إزالة التعريب…");
            try
            {
                await Task.Run(delegate
                {
                    string arabic = Path.GetFullPath(Path.Combine(root, "game", "tl", "arabic"));
                    string expectedParent = Path.GetFullPath(Path.Combine(root, "game", "tl")) + Path.DirectorySeparatorChar;
                    if (arabic.StartsWith(expectedParent, StringComparison.OrdinalIgnoreCase) && Directory.Exists(arabic)) Directory.Delete(arabic, true);
                    DeleteFile(Path.Combine(root, "game", "zz_arabic_support.rpy"));
                    DeleteFile(Path.Combine(root, "game", "zz_arabic_support.rpyc"));
                    DeleteFile(Path.Combine(root, "game", "NotoSansArabic.ttf"));
                    DeleteFile(Path.Combine(root, "ARABIC_LOCALIZATION_README.txt"));
                });
                progress.Value = 100;
                statusLabel.ForeColor = Color.FromArgb(128, 214, 154);
                statusLabel.Text = "تمت إزالة التعريب. النسخ الاحتياطية، إن وجدت، ما زالت محفوظة.";
            }
            catch (Exception ex)
            {
                statusLabel.ForeColor = Color.FromArgb(239, 107, 112);
                statusLabel.Text = "تعذرت الإزالة: " + ex.Message;
            }
            finally { SetBusy(false, null); }
        }

        private void SetBusy(bool busy, string message)
        {
            installButton.Enabled = !busy && IsValidGameDirectory(pathBox.Text.Trim());
            uninstallButton.Enabled = !busy && IsValidGameDirectory(pathBox.Text.Trim());
            browseButton.Enabled = !busy;
            pathBox.Enabled = !busy;
            if (busy) { progress.Value = 0; statusLabel.ForeColor = Color.FromArgb(187, 201, 222); statusLabel.Text = message; }
        }

        private static void DeleteFile(string path) { if (File.Exists(path)) File.Delete(path); }

        private static string RelativeTo(string root, string path)
        {
            return path.Substring(root.TrimEnd(Path.DirectorySeparatorChar).Length).TrimStart(Path.DirectorySeparatorChar);
        }

        private static void CopyDirectory(string source, string destination)
        {
            Directory.CreateDirectory(destination);
            foreach (string file in Directory.GetFiles(source)) File.Copy(file, Path.Combine(destination, Path.GetFileName(file)), true);
            foreach (string directory in Directory.GetDirectories(source)) CopyDirectory(directory, Path.Combine(destination, Path.GetFileName(directory)));
        }

        private static string FindGameDirectory()
        {
            List<string> roots = new List<string>();
            string current = AppDomain.CurrentDomain.BaseDirectory;
            if (File.Exists(Path.Combine(current, GameExe))) return current.TrimEnd(Path.DirectorySeparatorChar);
            string steam = ReadSteamPath();
            if (!String.IsNullOrEmpty(steam)) roots.Add(steam);
            foreach (DriveInfo drive in DriveInfo.GetDrives())
            {
                if (!drive.IsReady) continue;
                roots.Add(Path.Combine(drive.RootDirectory.FullName, "SteamLibrary"));
                roots.Add(Path.Combine(drive.RootDirectory.FullName, "Program Files (x86)", "Steam"));
            }
            foreach (string root in roots)
            {
            string candidate = Path.Combine(root, "steamapps", "common", "ALLBLACK Phase 2", "ALLBLACKPhase2-0.1-market");
                if (File.Exists(Path.Combine(candidate, GameExe))) return candidate;
                candidate = Path.Combine(root, "steamapps", "common", "ALLBLACK Phase 2");
                if (File.Exists(Path.Combine(candidate, GameExe))) return candidate;
            }
            return null;
        }

        private static string ReadSteamPath()
        {
            string[] keys = { @"HKEY_CURRENT_USER\Software\Valve\Steam", @"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Valve\Steam" };
            foreach (string key in keys)
            {
                object value = Registry.GetValue(key, "SteamPath", null) ?? Registry.GetValue(key, "InstallPath", null);
                if (value != null && Directory.Exists(value.ToString())) return value.ToString();
            }
            return null;
        }
    }
}
