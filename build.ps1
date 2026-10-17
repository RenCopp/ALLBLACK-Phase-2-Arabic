$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$payloadPath = Join-Path $projectRoot "payload"
$archivePath = Join-Path $projectRoot "payload-build.zip"
$outputPath = Join-Path $projectRoot "ALLBLACK-Phase-2-Arabic-Setup.exe"
$compiler = "$env:WINDIR\Microsoft.NET\Framework\v4.0.30319\csc.exe"
if (-not (Test-Path -LiteralPath $compiler)) { throw "The .NET Framework C# compiler was not found." }
if (Test-Path -LiteralPath $archivePath) { Remove-Item -LiteralPath $archivePath -Force }
Compress-Archive -Path (Join-Path $payloadPath "*") -DestinationPath $archivePath -CompressionLevel Optimal
& $compiler /nologo /target:winexe /optimize+ /platform:anycpu `
    "/win32manifest:$projectRoot\src\app.manifest" `
    /reference:System.Windows.Forms.dll /reference:System.Drawing.dll `
    /reference:System.IO.Compression.dll /reference:System.IO.Compression.FileSystem.dll `
    "/resource:$archivePath,Payload.Zip" "/out:$outputPath" "$projectRoot\src\Program.cs"
if ($LASTEXITCODE -ne 0) { throw "Installer compilation failed with exit code $LASTEXITCODE." }
Get-FileHash -LiteralPath $outputPath -Algorithm SHA256
