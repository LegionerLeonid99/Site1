# PowerShell script to move contents from Gau folder to repository root
# Run this script from e:\Site1 directory

Write-Host "Moving files from Gau folder to repository root..." -ForegroundColor Green

# Get the current location
$currentDir = Get-Location
Write-Host "Current directory: $currentDir"

# Check if we're in Site1 directory
if ($currentDir.Path -notmatch "Site1$") {
    Write-Host "Please navigate to e:\Site1 directory first!" -ForegroundColor Red
    Write-Host "Run: cd e:\Site1" -ForegroundColor Yellow
    exit 1
}

# Check if Gau folder exists
if (-not (Test-Path "Gau")) {
    Write-Host "Gau folder not found!" -ForegroundColor Red
    exit 1
}

Write-Host "Starting file move operation..." -ForegroundColor Yellow

# Move all files and folders from Gau to current directory
Get-ChildItem -Path "Gau" -Force | ForEach-Object {
    $destination = Join-Path -Path $currentDir -ChildPath $_.Name
    
    if (Test-Path $destination) {
        Write-Host "Skipping $($_.Name) - already exists in destination" -ForegroundColor Yellow
    } else {
        Write-Host "Moving $($_.Name)..." -ForegroundColor Cyan
        Move-Item -Path $_.FullName -Destination $currentDir -Force
    }
}

Write-Host "`nFile move completed!" -ForegroundColor Green
Write-Host "Checking if Gau folder is empty..." -ForegroundColor Yellow

# Check if Gau folder is empty
$gauContents = Get-ChildItem -Path "Gau" -Force
if ($gauContents.Count -eq 0) {
    Write-Host "Gau folder is empty. Removing..." -ForegroundColor Green
    Remove-Item "Gau" -Force
    Write-Host "Gau folder removed successfully!" -ForegroundColor Green
} else {
    Write-Host "Gau folder still contains files:" -ForegroundColor Yellow
    $gauContents | ForEach-Object { Write-Host "  - $($_.Name)" }
    Write-Host "`nPlease check and manually remove remaining files." -ForegroundColor Yellow
}

Write-Host "`n=== Operation Complete ===" -ForegroundColor Green
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Review the moved files"
Write-Host "2. Run: git add ."
Write-Host "3. Run: git commit -m 'Restructure: move project to repository root'"
Write-Host "4. Run: git push origin main"
