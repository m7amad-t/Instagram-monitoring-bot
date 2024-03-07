<body>
  <h1>Instagram Profile Monitor Bot</h1>
  
  <h2>Overview</h2>
  <p>This Python script monitors changes to an Instagram user's profile and notifies via Telegram when changes occur. It fetches data from the Instagram API endpoint, compares it with the previous data, and sends a notification if any changes are detected.</p>
  
  <h2>Features</h2>
  <ul>
    <li>Monitors Instagram profile for changes in name, bio, followers count, following count, post count, account privacy, profile picture, and external links.</li>
    <li>Sends notifications via Telegram when changes are detected.</li>
    <li>Periodically checks for changes at hourly intervals.</li>
  </ul>
  <br>
  <h2>Prerequisites</h2>
  <ul>
    <li>Python 3.x installed on your system.</li>
    <li>Required Python packages: <code>requests</code>, <code>time</code>.</li>
  </ul>
  <br><br>
  <h2>Installation</h2>
  <ol>
    <li>Clone this repository to your local machine.</li>
    <li>Install dependencies using pip:</li>
  </ol>
  <pre><code>pip install -r requirements.txt</code></pre>
  <br><br>
  <h2>Configuration</h2>
  <ol>
    <li>Replace <code>YOUR_BOT_TOKEN</code> and <code>YOUR_CHAT_ID</code> in the script with your Telegram Bot token and chat ID respectively.</li>
    <li>Modify the <code>username</code> variable in the script to specify the Instagram username you want to monitor.</li>
    <li>Update the <code>headers</code> variable in the script with the necessary headers (cookies) obtained from inspecting the Instagram API request in your browser.</li>
  </ol>
  <br><br>
  <h2>Notes</h2>
    <ol>
      <li>Go to <a href="https://t.me/BotFather">Bot_father</a> crate a bot then copy your bot's <code>BOT_TOKEN</code>, replace it.</li>
      <li>Go to <a href="https://t.me/RawDataBot">Row_data_bot</a> send <code>/start</code> get your  <code>CHAT_ID</code>, replace it.</li>
      <li>Go to Instagram, login to an account then go to the profile that you want to follow. open inspect <code>(click right -> inspect)</code> or <code>(Ctrl+Shift+j)</code> go to <Strong>Network</Strong> filter only XHR files find this Request "<strong> <i>https://www.instagram.com/api/v1/users/web_profile_info/?username=_____</i> </strong>" then copy <code>Request Headers</code>, replace it.</li>
    </ol>
  <br><br>
  <h2>Techniques and Technologies Used</h2>
  <p>The Instagram Profile Monitor Bot utilizes several techniques and technologies to achieve its functionality:</p>
  <ol>
    <li><strong>Reverse Engineering Instagram's API:</strong> The project involves reverse engineering Instagram's API to understand its communication protocol and endpoints.</li>
    <br>
    <li><strong>Network Traffic Analysis:</strong> Network traffic analysis is used to capture and inspect HTTP requests and responses exchanged between the client application and Instagram's servers.</li>
    <br>
    <li><strong>Python Scripting:</strong> Python is used as the primary programming language for developing the monitoring bot, leveraging its libraries for making HTTP requests, data manipulation, and bot functionality.</li>
    <br>
    <li><strong>Telegram Bot Integration:</strong> The bot integrates with the Telegram Bot API to send real-time notifications to users when changes are detected in monitored profiles.</li>
    <br>
    <li><strong>Periodic Monitoring and Notification:</strong> The bot is designed to periodically fetch profile data from Instagram's API and send notifications via Telegram when changes are detected.</li>
    <br>
    <li><strong>Security and Privacy Considerations:</strong> Measures are taken to ensure the secure handling of user data and compliance with Instagram's terms of service and usage agreements.</li>
  </ol>
  <br><br>
  <h2>Usage</h2>
  <p>Run the script using Python:</p>
  <pre><code>python instagram_profile_monitor.py</code></pre>
  <br><br>
  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
