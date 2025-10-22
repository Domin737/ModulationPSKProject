# FILES TO DELETE FROM REPOSITORY

## ❌ COMPLETE DELETION LIST

These files should be **DELETED** before deploying the new complete implementation.

---

## 🗑️ OUTDATED SOURCE FILES IN `src/`

### 1. **src/TransmissionChannel.py**
**Reason:** Empty file
**Status:** DELETE and replace with new version

### 2. **src/Demodulator.py**
**Reason:** Nearly empty (only has `from AddAWGNNoise import *`)
**Status:** DELETE and replace with complete version

### 3. **src/main.py**
**Reason:** Just skeleton with no real functionality
**Status:** DELETE and replace with complete simulation

### 4. **src/Modulator.py** (CONDITIONAL)
**Check first:** Does it have QPSK, 8-PSK, and 16-QAM?
**If NO:** DELETE and replace with complete version
**If YES:** Keep it (but verify it's correct)

---

## 🗑️ OUTDATED DOCUMENTATION IN `docs/`

### Option A: Delete Entire `docs/` Folder (Recommended)

```bash
rm -rf docs/
```

**Reason:** All documentation is now in the main README.md

### Option B: Delete Individual Files

If you want to keep the `docs/` folder:

1. **docs/CODE_REVIEW.md**
   - Says project "needs implementation"
   - Status: **DELETE**

2. **docs/PODSUMOWANIE.md**
   - Says "30% complete"
   - Status: **DELETE**

3. **docs/PROJECT_ARCHITECTURE.md**
   - Says "needs work"
   - Status: **DELETE**

4. **docs/INSTALLATION.md** (Optional)
   - Can keep if accurate
   - Or DELETE - info is in README.md

5. **docs/QUICKSTART.md** (Optional)
   - Can keep if accurate
   - Or DELETE - we have new QUICK_START.md in root

6. **docs/INDEX.md** (Optional)
   - May be outdated
   - Check references to test files

7. **docs/README.md** (Optional)
   - Check if accurate
   - We have new README.md in root

---

## 🗑️ ROOT LEVEL FILES

### 1. **TransmissionChannel.py** (in root, if exists)
**Reason:** Empty duplicate file
**Status:** DELETE (file should only be in `src/`)

### 2. **Zadanie.jpg** (Optional)
**Reason:** Original assignment image
**Options:**
- Keep for reference
- Or DELETE to clean up repo

---

## 🗑️ TEST FILES (If they exist and are broken)

### **tests/test_environment.py**
**Check:** Does this file exist and work?
**If broken:** DELETE
**If working:** Keep it

### Entire `tests/` folder (Optional)
**If folder exists but tests don't work:** DELETE
**Reason:** New code has built-in tests in each module

---

## 🗑️ TEMPORARY/CACHE FILES

Always delete:
```
__pycache__/
*.pyc
*.pyo
*.pyd
.DS_Store
Thumbs.db
*.swp
*.swo
*~
```

---

## 📋 DELETION CHECKLIST

### Step 1: Backup First!
```bash
git add .
git commit -m "Backup before cleanup"
git branch backup-before-cleanup
```

### Step 2: Delete Outdated Source Files
```bash
cd src
rm TransmissionChannel.py  # Empty
rm Demodulator.py          # Nearly empty
rm main.py                 # Skeleton

# ONLY if Modulator.py is incomplete:
# rm Modulator.py
```

### Step 3: Delete Outdated Documentation (Option A - Recommended)
```bash
cd ..
rm -rf docs/
```

### Step 3 Alternative: Delete Individual Doc Files (Option B)
```bash
rm docs/CODE_REVIEW.md
rm docs/PODSUMOWANIE.md
rm docs/PROJECT_ARCHITECTURE.md
# Optionally delete others
```

### Step 4: Delete Root Level Duplicates
```bash
rm TransmissionChannel.py 2>/dev/null || true
# Optionally:
# rm Zadanie.jpg
```

### Step 5: Delete Test Files (if broken)
```bash
rm -rf tests/ 2>/dev/null || true
```

### Step 6: Clean Cache
```bash
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete
```

---

## 🛡️ SAFE DELETION SCRIPT

Create this script and run it:

```bash
#!/bin/bash
# cleanup.sh

echo "Starting cleanup..."

# Backup first
git add .
git commit -m "Backup before major cleanup"
git branch backup-$(date +%Y%m%d)

# Delete outdated source files
echo "Deleting outdated source files..."
rm -f src/TransmissionChannel.py
rm -f src/Demodulator.py
rm -f src/main.py

# Delete docs folder (or use selective deletion)
echo "Deleting outdated documentation..."
rm -rf docs/
# OR selectively:
# rm -f docs/CODE_REVIEW.md
# rm -f docs/PODSUMOWANIE.md
# rm -f docs/PROJECT_ARCHITECTURE.md

# Delete root duplicates
echo "Deleting root duplicates..."
rm -f TransmissionChannel.py

# Delete cache
echo "Cleaning cache..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true

echo "Cleanup complete!"
echo ""
echo "Deleted files summary:"
echo "  - Outdated source files in src/"
echo "  - Outdated documentation"
echo "  - Cache files"
echo ""
echo "Next steps:"
echo "  1. Copy new files from final_code/"
echo "  2. Run setup.sh (or setup.bat)"
echo "  3. Test the application"
```

---

## ⚠️ IMPORTANT NOTES

### DON'T Delete These:

✅ **src/GetBytes.py** - Keep (it's good)
✅ **src/AddAWGNNoise.py** - Keep (it's perfect)
✅ **requirements.txt** - Update if needed, but don't delete
✅ **.gitignore** - Update with new version
✅ **.gitattributes** - Add if missing
✅ **README.md** - Replace with new version

### Conditional Files:

⚠️ **src/Modulator.py**
- Check if it has all 4 modulations
- If ONLY BPSK → DELETE and replace
- If complete → Keep (but verify)

⚠️ **docs/** folder
- Recommended: DELETE entire folder
- Alternative: Update each file individually
- Reason: New README.md is comprehensive

⚠️ **Zadanie.jpg**
- Keep for reference
- Or delete to clean up
- Your choice

---

## 🎯 AFTER DELETION

Your repository should have:

```
ModulationPSKProject/
├── src/
│   ├── GetBytes.py           ✅ (updated or kept)
│   ├── AddAWGNNoise.py       ✅ (kept)
│   └── [empty - ready for new files]
├── results/
│   └── [empty or with .gitkeep]
├── requirements.txt           ✅ (update if needed)
├── .gitignore                ✅ (update)
└── README.md                 ✅ (replace)
```

Then copy all new files from `final_code/`.

---

## 📊 SUMMARY

### Files to DELETE:
- ❌ src/TransmissionChannel.py (empty)
- ❌ src/Demodulator.py (nearly empty)
- ❌ src/main.py (skeleton)
- ❌ docs/CODE_REVIEW.md (outdated)
- ❌ docs/PODSUMOWANIE.md (outdated)
- ❌ docs/PROJECT_ARCHITECTURE.md (outdated)
- ❌ TransmissionChannel.py (root duplicate)
- ❌ __pycache__/ (cache)

### Files to UPDATE:
- 🔄 src/Modulator.py (if incomplete)
- 🔄 README.md (replace)
- 🔄 .gitignore (replace)

### Files to KEEP:
- ✅ src/GetBytes.py
- ✅ src/AddAWGNNoise.py
- ✅ requirements.txt

---

## ✅ VERIFICATION

After deletion, verify:

```bash
# Should only see these Python files in src/:
ls src/*.py
# Output should be:
#   src/GetBytes.py
#   src/AddAWGNNoise.py
# (and maybe Modulator.py if it's complete)

# Docs folder should be gone:
ls docs/ 2>&1
# Output should be: No such file or directory
# (unless you kept it)

# No cache:
find . -name "__pycache__"
# Output should be: (empty)
```

---

**Ready to delete?** Follow the checklist above!

**Need help?** See DEPLOYMENT_GUIDE.md

---

**Version:** 1.0.0  
**Date:** 2025-10-22  
**Type:** Cleanup Instructions
