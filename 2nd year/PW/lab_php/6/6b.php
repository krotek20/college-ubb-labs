<?php

    session_start();

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "labphp";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $content = "<h2>20.2 Patch Notes</h2><br>
    Quilboar have been added as a new Battlegrounds minion type! There will still be five minion types per Battlegrounds game once Quilboar are added, meaning that three minion types will be excluded from each game. Just like when Dragons, Pirates, and Elementals were added, Quilboar will show up in every Battlegrounds match until our next major content patch.<br>
    The Quilboar update includes 17 new minions, 3 new heroes, and a new mechanic: Blood Gems! Blood Gems are spells that give a friendly minion +1/+1. Some Quilboar give you Blood Gems, while others have special interactions when Blood Gems are played.<br>
    We’ve also added Battlegrounds support for your favorite Coin! As a reminder, you can set a Coin as your favorite by clicking on the Coin icon in the top right of your Collection.<br>
    Finally, prepare for a fresh playing field as all players’ Battlegrounds ratings will be reset to 0 when the 20.2 patch launches on May 4!<br><br>";

    if (isset($_GET["user"])) {
        $username = addslashes(htmlentities($_GET["user"], ENT_COMPAT, "UTF-8"));
        if ($username == "" || strlen($username) > 255) {
            session_destroy();
            header("Location: 6.html");
            exit();
        }
        if ($_SESSION["user"] == $username) {
            $sql = "SELECT * FROM comentarii";
            $stmt = $conn->prepare($sql);
            $stmt->execute();
            $stmt->bind_result($id, $user, $comment, $state);
            while ($stmt->fetch()) {
                if ($state == 0) {
                    $content .= "<form action='6c.php' method='POST'>
                    <input type='hidden' name='id' value='$id'>
                    <input type='hidden' name='username' value='$username'>
                    <label>$user</label><br>
                    <label>$comment</label><br>
                    <input type='submit' value='Confirm'>
                    </form>
                    <form action='6e.php' method='POST'>
                    <input type='hidden' name='id' value='$id'>
                    <input type='hidden' name='username' value='$username'>
                    <input type='submit' value='Cancel'>
                    </form>";
                }
                else {
                    $content .= "<label>$user</label><br><label>$comment</label>";
                }
                $content .= "<br><br>";
            }
        }
    }
    else {
        $sql = "SELECT user, comment FROM comentarii WHERE state = 1";
        $stmt = $conn->prepare($sql);
        $stmt->execute();
        $stmt->bind_result($user, $comment);

        while ($stmt->fetch()) {
            $content .= "<label>$user</label><br><label>$comment</label><br><br>";
        }

        $content .= "<form action='6d.php' method='POST'>
        <label>Nume</label>
        <input type='text' name='user'/><br>
        <label>Comment</label>
        <input type='text' name='comment'/><br>
        <input type='submit' value='Submit'>
        </form>";
    }

    echo $content;

?>