
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
    <h2>Prerequisites</h2>
    <ul>
      <li>Python 3.x installed on your system.</li>
      <li>Required Python packages: <code>requests</code>, <code>time</code>.</li>
    </ul>
    <h2>Installation</h2>
    <ol>
      <li>Clone this repository to your local machine.</li>
      <li>Install dependencies using pip:</li>
    </ol>
    <pre><code>pip install -r requirements.txt</code></pre>
    <h2>Configuration</h2>
    <ol>
      <li>Replace <code>YOUR_BOT_TOKEN</code> and <code>YOUR_CHAT_ID</code> in the script with your Telegram Bot token and chat ID respectively.</li>
      <li>Modify the <code>username</code> variable in the script to specify the Instagram username you want to monitor.</li>
      <li>Update the <code>headers</code> variable in the script with the necessary headers (cookies) obtained from inspecting the Instagram API request in your browser.</li>
    </ol>
    <h2>Notes</h2>
    <ol>
      <li>Go to <a href="https://t.me/BotFather">Bot_father</a> crate a bot then copy your bot's <code>BOT_TOKEN</code>, replace it.</li>
      <li>Go to <a href="https://t.me/RawDataBot">Row_data_bot</a> send <code>/start</code> get your  <code>CHAT_ID</code>, replace it.</li>
      <li>Go to Instagram, login to an account then go to the profile that you want to follow. open inspect <code>(click right -> inspect)</code> or <code>(Ctrl+Shift+j)</code> go to <Strong>Network</Strong> filter only XHR files find this Request "<strong> <i>https://www.instagram.com/api/v1/users/web_profile_info/?username=_____</i> </strong>" then copy <code>Request Headers</code>, replace it.</li>
    </ol>
    <h2>Usage</h2>
    <p>Run the script using Python:</p>
    <pre><code>python instagram_profile_monitor.py</code></pre>
    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
  </body>

