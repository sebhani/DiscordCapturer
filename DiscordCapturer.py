import pyimgur
import requests
import json
import pyautogui

#take capture of screen
localPath  = #<Where_To_Save_Capture>
myScreenshot = pyautogui.screenshot()
myScreenshot.save(localPath)

# upload to imgur
CLIENT_ID = #<imgur_client_ID>

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(localPath, title="Uploaded with PyImgur")
# print(uploaded_image.title)
# print(uploaded_image.link)
# print(uploaded_image.size)
# print(uploaded_image.type)


# send to discord
url = #<Discord_Webhook> --> Go to channel settings --> Integrations --> create a webhook

payload = json.dumps({
  "content": "url: "+uploaded_image.link,
  "embeds": [
    {
      "image": {
        "url": uploaded_image.link
      }
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

print("sent!")
# print(response.text)