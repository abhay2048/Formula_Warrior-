# Formula Warrior - GitHub Actions Build Instructions

This repository contains a Kivy-based quiz app and a GitHub Actions workflow that attempts to build
an Android debug APK using Buildozer on an Ubuntu runner.

IMPORTANT: I cannot build the APK for you in this environment. This workflow will run *when you push
the repository to GitHub*. Builds that download the Android SDK/NDK can be heavy and may require
tweaking. If the workflow fails, read the Actions log and paste the error output back here.

## How to use (button-by-button for Windows users)

1. Go to https://github.com and **Sign in** or **Create an account**.
2. Click the **+** icon (top-right) → **New repository**.
   - Repository name: `formula_warrior`
   - Set it **Public** (or Private)
   - Click **Create repository**
3. On your Windows PC, open **File Explorer** → go to the folder where you downloaded this project ZIP → extract it.
4. Open **Git Bash** (install Git for Windows first if you don't have it).
5. In Git Bash, run these commands (replace with your GitHub repo URL shown on the new repo page):
   ```
   cd /c/Users/<YourUser>/Downloads/formula_warrior_github_build
   git init
   git add .
   git commit -m "Initial commit - formula warrior"
   git branch -M main
   git remote add origin https://github.com/<YourUser>/formula_warrior.git
   git push -u origin main
   ```
6. After pushing, go to your GitHub repository page → click **Actions** tab.
   - The workflow `.github/workflows/build.yml` will start automatically.
   - Click the running workflow to see logs. If it finishes successfully, artifacts will appear under the job's **Artifacts** section.
7. Click **Artifacts** → download the debug APK artifact (if the workflow uploaded it).

## If the build fails
- Copy the last 50 lines of the Actions log and paste them back here.
- I’ll help you debug and patch the workflow.

## Notes
- Building an Android APK requires significant disk space and time. GitHub Actions runners provide limited resources.
- If this workflow fails due to runner limitations, consider building on a local Linux VM or using a paid CI with more resources.
