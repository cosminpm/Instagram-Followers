# instagram_followers

This code gets you the difference between two sets of followers.

#### This code allows you to:
- Know who you are following you and if they do not follow you.
- Know who follows you and you are not following.

#### How to use it?
  1. Go to the instagram profile you want, in this example we used _PSG_ account.
  <p align="center">
    <img src="./images/1-Where.JPG" alt="drawing" width="500"/>
  </p>
  2. Open the developer tools, elements and copy the body.
  <p align="center">
     <img src="./images/2-Developer.JPG" alt="drawing" width="500"/>
  </p>

  3. Paste it on Followers.txt
  4. To the same for Following.txt
  5. In the _main_ function change write_to_file if you want the difference from _A to B_ or _B to A_. 
  6. Run the script. In the directory you will find a new file _accounts.txt_ with the information you requested
 
 **Attention: The only throback is that you can't get all the followers if they haven't been loaded in the browser.**
