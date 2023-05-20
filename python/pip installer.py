import pip
print("Package Installer".center(50))
pkgName=input("Enter package name: ")
pip.main(['install',pkgName])