<!DOCTYPE html>
<html lang="en">
<body>

<h1>🏆 Discord Matchmaking Bot</h1>

<p>A Python bot for managing <span class="highlight">1v1 matches</span> on Discord. It automates queue management, match reporting, and tracks player scores.</p>

<h2>⚙️ Features:</h2>
<ul>
    <li><strong>Queue System:</strong> Players join with the <span class="command">!j</span> command and leave with <span class="command">!l</span>. When 2 players are in the queue, a match is set.</li>
    <li><strong>Match Reporting:</strong> Players report match results with a screenshot and mention in the match report channel. The bot verifies and updates scores.</li>
    <li><strong>Score Tracking:</strong> The bot automatically updates scores in players' nicknames based on match results.</li>
</ul>

<h2>📦 Setup:</h2>
<ol>
    <li>Install the <code>discord.py</code> library:
        <pre><code>pip install discord.py</code></pre>
    </li>
    <li>Insert your bot token, server ID, and match report channel ID into the code.</li>
    <li>Run the bot.</li>
</ol>

</body>
</html>
