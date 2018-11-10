<html>
<head>
    <title> Chat Room Login </title>
</head>
    <link rel="stylesheet" type="text/css" href="chatindex1.css">
    <?php
    session_start();
    ?>

    <body>
        <div class="loginbox">
            <img src="avatar.png" class="avatar">
            <h1>Create Username Here</h1>
                <form action="chatroom.php" method="POST" autocomplete="off">
                    <p> Username </p>
                    <input type="text" name="username" placeholder="Enter Username">
                    <p> Email </p>
                    <input type="text" name="email" placeholder="Enter an Email">
                    <input type="submit" name="Enter"/>
                </form>
        </div>
    </body>
</html>
