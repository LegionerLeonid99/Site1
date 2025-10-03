# QUICK START - Restructure Repository

## The Fastest Way

### Using PowerShell (Recommended):

```powershell
# 1. Navigate to repository root
cd e:\Site1

# 2. Run the move script
.\Gau\move-to-root.ps1

# 3. Commit and push
git add .
git commit -m "Restructure: move project to repository root"
git push origin main
```

### Using Batch Script:

```cmd
# 1. Navigate to repository root
cd e:\Site1

# 2. Run the batch script
Gau\move-to-root.bat

# 3. Commit and push
git add .
git commit -m "Restructure: move project to repository root"  
git push origin main
```

### Using Manual Commands:

```powershell
cd e:\Site1
Get-ChildItem -Path "Gau" -Force | Move-Item -Destination . -Force
Remove-Item "Gau" -Force
git add .
git commit -m "Restructure: move project to repository root"
git push origin main
```

## What Happens After Push?

1. ✅ Railway detects changes automatically
2. ✅ Railway finds config files in root
3. ✅ Railway builds project correctly
4. ✅ Site deploys successfully
5. ✅ Available at your Railway URL

## Time Required
- Move files: 2 minutes
- Commit/push: 2 minutes  
- Railway deploy: 5-10 minutes
- **Total: ~15 minutes**

## Files You Have

Three options to move files:
1. **move-to-root.ps1** - PowerShell script (best for Windows 10+)
2. **move-to-root.bat** - Batch script (works on all Windows)
3. **Manual commands** - See RESTRUCTURE_GUIDE.md

## Need Help?

See **RESTRUCTURE_GUIDE.md** for:
- Detailed step-by-step instructions
- Troubleshooting
- Verification steps
- What to do if something goes wrong

---

**Ready? Let's go!** 🚀

```powershell
cd e:\Site1
.\Gau\move-to-root.ps1
```
