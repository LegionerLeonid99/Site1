# Railway Configuration - Repository Root Setup

## Problem
Railway is looking at your GitHub repository root, but the project files are inside the `Gau` folder.

## Solution Options

### Option 1: Configure Railway Root Directory (RECOMMENDED)

In Railway Dashboard:
1. Go to your project Settings
2. Find "Root Directory" or "Working Directory" setting
3. Set it to: `Gau`
4. Save and redeploy

This tells Railway to treat the `Gau` folder as the project root.

### Option 2: Move Configuration Files to Repository Root

If Railway doesn't have a root directory setting, you need to:

1. **Copy these files from `Gau/` to the repository root (parent directory):**
   - `nixpacks.toml`
   - `railway.json`
   - `Procfile`
   - `start.sh`
   - `Dockerfile`
   - `.dockerignore`

2. **Update the copied files** to include `Gau/` prefix:

**In root `nixpacks.toml`:**
```toml
[phases.setup]
nixPkgs = ["nodejs-18_x", "python310"]

[phases.install]
cmds = [
    "cd Gau && npm install",
    "cd Gau && pip install -r backend/requirements.txt",
    "pip install gunicorn"
]

[phases.build]
cmds = ["cd Gau && npm run build"]

[start]
cmd = "cd Gau/backend && cp -r ../dist ./static && gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 app:app"
```

**In root `railway.json`:**
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "cd Gau && npm install && npm run build && cd backend && pip install -r requirements.txt && pip install gunicorn"
  },
  "deploy": {
    "startCommand": "cd Gau/backend && gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 app:app",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

**In root `Procfile`:**
```
web: cd Gau/backend && gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 app:app
```

**In root `start.sh`:**
```bash
#!/bin/bash
cd Gau
npm install
npm run build
cd backend
pip install -r requirements.txt
pip install gunicorn
gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 app:app
```

3. **Commit and push:**
```bash
git add .
git commit -m "Move Railway config to repository root"
git push origin main
```

### Option 3: Restructure Repository

Move all files from `Gau/` to repository root:
1. Move everything up one level
2. Delete empty `Gau/` folder
3. Keep the configuration files as they are now

## How to Execute Option 2 (Step by Step)

### Using Command Line:

```bash
# Navigate to repository root (parent of Gau)
cd e:\Site1

# Copy configuration files to root
copy Gau\nixpacks.toml nixpacks.toml
copy Gau\railway.json railway.json  
copy Gau\Procfile Procfile
copy Gau\start.sh start.sh
copy Gau\Dockerfile Dockerfile
copy Gau\.dockerignore .dockerignore

# Edit the copied files to add "Gau/" prefix to all paths
# (Use notepad or VS Code to edit each file)

# Commit and push
git add .
git commit -m "Add Railway config files to repository root"
git push origin main
```

### Using VS Code:

1. Open the parent folder (`e:\Site1`) in VS Code
2. You should see:
   ```
   Site1/
   ├── Gau/
   │   ├── package.json
   │   ├── backend/
   │   ├── src/
   │   └── ...
   ```
3. Copy the configuration files from `Gau/` to `Site1/` root
4. Edit each copied file to add `Gau/` prefix as shown above
5. Commit and push

## Verify Repository Structure

Your GitHub repository should look like:

```
Site1/                          <- Repository root (Railway looks here)
├── nixpacks.toml              <- Railway config
├── railway.json               <- Railway config
├── Procfile                   <- Railway config  
├── start.sh                   <- Railway config
├── Dockerfile                 <- Railway config
├── .dockerignore              <- Railway config
└── Gau/                       <- Your project
    ├── package.json
    ├── backend/
    │   ├── app.py
    │   └── ...
    ├── src/
    └── ...
```

## Current Status

The configuration files in `Gau/` folder are set up correctly for when the working directory is `Gau/`.

**You need to either:**
- Set Railway Root Directory to `Gau` (Option 1 - easiest)
- OR copy configs to repository root with `Gau/` prefixes (Option 2)

## Recommended: Option 1

Try Option 1 first! In Railway:
- Settings → General → Root Directory → Set to `Gau`
- This is the cleanest solution

If Root Directory setting doesn't exist, use Option 2.
