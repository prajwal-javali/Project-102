import time
import random
import cv2
import dropbox

startTime = time.time()

def takesnapshot():
    num = random.randint(0, 100)
    object = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = object.read()
        imageName = "pic" + str(num) + ".png"
        cv2.imwrite(imageName, frame)
        startTime = time.time()
        result = False
    return imageName
    print("Picture Taken")
    object.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    accessToken = 'Ybo_mLO8ihEAAAAAAAAAATHBvsVat3jcTfnGIFHLLVs4HKhWqozdrjV1pRoNlxvZ'
    fileFrom = imageName
    fileto = "/class 102/" + imageName
    dbx = dropbox.Dropbox(accessToken)
    with open(fileFrom, "rb") as f:
        dbx.files_upload(f.read(), fileto, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if ((time.time()- startTime) >= 30):
            name = takesnapshot()
            uploadFile(name)

main()
