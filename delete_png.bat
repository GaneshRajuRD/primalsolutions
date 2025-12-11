@echo off
for %%f in (public\assets\image\*.png) do (
    if exist "%%~dpnf.webp" (
        del "%%f"
    )
)
echo PNG files with WEBP counterparts have been deleted.
