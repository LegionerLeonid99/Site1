# Guide: Restructure Repository - Remove Gau Folder

## What This Does
Moves all contents from `Site1/Gau/` to `Site1/` (repository root) and removes the empty Gau folder.

## Before You Start

### 1. Commit Current Changes
Make sure all current changes in Gau folder are committed:
```powershell
cd e:\Site1\Gau
git add .
git commit -m "Prepare for repository restructure"
git push origin main
```

### 2. Backup (Optional but Recommended)
Create a backup of the Gau folder:
```powershell
cd e:\Site1
Copy-Item -Path "Gau" -Destination "Gau_backup" -Recurse
```

## Step-by-Step Instructions

### Option 1: Using the PowerShell Script (RECOMMENDED)

1. **Navigate to repository root:**
   ```powershell
   cd e:\Site1
   ```

2. **Run the move script:**
   ```powershell
   .\Gau\move-to-root.ps1
   ```

3. **Verify the move:**
   ```powershell
   # List files in current directory
   Get-ChildItem
   
   # Should now see all project files here
   ```

4. **Commit the changes:**
   ```powershell
   git add .
   git commit -m "Restructure: move project to repository root"
   git push origin main
   ```

### Option 2: Manual Move

1. **Navigate to repository root:**
   ```powershell
   cd e:\Site1
   ```

2. **Move all files and folders:**
   ```powershell
   # Move all items from Gau to current directory
   Get-ChildItem -Path "Gau" -Force | Move-Item -Destination . -Force
   ```

3. **Remove empty Gau folder:**
   ```powershell
   Remove-Item "Gau" -Force
   ```

4. **Commit changes:**
   ```powershell
   git add .
   git commit -m "Restructure: move project to repository root"
   git push origin main
   ```

### Option 3: Using File Explorer

1. Open File Explorer
2. Navigate to `e:\Site1\Gau`
3. Select all files and folders (Ctrl+A)
4. Cut (Ctrl+X)
5. Navigate up to `e:\Site1`
6. Paste (Ctrl+V)
7. Delete the empty `Gau` folder
8. In terminal:
   ```powershell
   cd e:\Site1
   git add .
   git commit -m "Restructure: move project to repository root"
   git push origin main
   ```

## After Moving

### Repository Structure Will Be:
```
Site1/                          <- Repository root
├── .dockerignore
├── .gitignore
├── .vscode/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── dist/
├── Dockerfile
├── index.html
├── nixpacks.toml              <- Railway will find these now!
├── node_modules/
├── package.json
├── Procfile
├── public/
├── railway.json
├── README.md
├── src/
├── start.sh
├── tailwind.config.js
└── vite.config.js
```

## Update Railway Configuration

After pushing to GitHub, Railway will automatically:
- ✅ Find `nixpacks.toml` in repository root
- ✅ Find `railway.json` in repository root
- ✅ Find `package.json` in repository root
- ✅ Find `backend/` folder
- ✅ Build and deploy correctly

**You don't need to change anything in Railway!** Just push and let it redeploy.

## Verify Deployment

1. **Railway will auto-deploy** when you push
2. **Check build logs** in Railway dashboard
3. **Test the site:**
   - Homepage: `https://your-app.railway.app`
   - API: `https://your-app.railway.app/api/health`

## Troubleshooting

### If files didn't move:
```powershell
# Check what's still in Gau
Get-ChildItem e:\Site1\Gau

# Move specific folders manually
Move-Item e:\Site1\Gau\backend e:\Site1\
Move-Item e:\Site1\Gau\src e:\Site1\
# etc...
```

### If git shows too many changes:
```powershell
# Stage all deletions and additions
git add -A
git commit -m "Restructure: move project to repository root"
```

### If Railway still fails:
Check that these files exist in repository root:
- `package.json`
- `nixpacks.toml` or `railway.json`
- `backend/requirements.txt`

## Important Notes

1. **Git will track this as moving files** - file history is preserved
2. **Railway will redeploy automatically** after push
3. **Environment variables in Railway stay the same** - no need to change
4. **All configuration files are already correct** - they don't reference "Gau" folder

## Clean Up

After successful deployment, you can delete the backup:
```powershell
cd e:\Site1
Remove-Item "Gau_backup" -Recurse -Force
```

## Expected Timeline

- Move files: 1-2 minutes
- Git commit/push: 1-2 minutes
- Railway detect changes: instant
- Railway build: 5-10 minutes
- Total: ~10-15 minutes

Your site will be live at the same Railway URL after successful deployment! 🚀
