import tkinter as tk
import tweepy as tp
# test

# Authenticate to Twitter
auth = tp.OAuthHandler("API TOKEN", "API SECRET TOKEN")
auth.set_access_token("ACCESS TOKEN", "SECRET ACCESS TOKEN")

# Create API object
api = tp.API(auth)

# Creates the window, disables resizing and sets the title to "kryntweet"
tweet= tk.Tk()
tweet.title("kryntweet")
tweet.resizable(False, False)

canvas1 = tk.Canvas(tweet, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(tweet, text="Write your tweet here.")
canvas1.create_window(200, 115, window=label1)

label2 = tk.Label(tweet, text="Your Tweet has been sent!")

entry1 = tk.Entry (tweet) 
canvas1.create_window(200, 140, window=entry1)

# Gets input from the entry box and tweets said input
def sendTweet():  
    x1 = entry1.get()
    
    api.update_status(x1 + " (☆)")
	
# If sending tweet is successful, the entry box will clear and "Your tweet has been sent!" will show up on screen.
def success():
	canvas1.create_window(200, 200, window=label2)
	entry1.delete(0, 'end')
	label2.after(2500, label2.destroy)

button1 = tk.Button(text='LMAO Send Tweet',command=lambda:[sendTweet(), success()])
canvas1.create_window(200, 170, window=button1)

# tweet.iconbitmap(r'C:\Program Files\Python36\kryntweet\kryntweet.ico')#
tweet.mainloop()
