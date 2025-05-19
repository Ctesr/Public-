from psd_tools import PSDImage

try:
    psd = PSDImage.open("D:\JCtestgit\Dome_project\PSD\Kỷ Niệm 11.psd")
    print("PSD 文件正常")
except Exception as e:
    print("PSD 文件损坏:", e)
