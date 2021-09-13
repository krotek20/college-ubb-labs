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

    $content = "";
    $profileString = "5b.php?user=%s";
    $deleteString = "5c.php?user=%s&id=%s";

    if (isset($_GET["user"])) {
        $username = addslashes(htmlentities($_GET["user"], ENT_COMPAT, "UTF-8"));

        if ($username == "" || strlen($username) > 255) {
            header("Location: 5.html");
            exit();
        }

        // load users
        $sqlUsers = "SELECT username FROM utilizatori WHERE username != ?";
        $stmt = $conn->prepare($sqlUsers);
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->bind_result($returnedUsername);

        while($stmt->fetch()) {
            $path = sprintf($profileString, $returnedUsername);
            $content .= "<a href='$path'>$returnedUsername</a>";
        }

        $content .= "<br><br>";

        // load images
        $sqlImages = "SELECT id, img FROM imagini WHERE username = ?";
        $stmt = $conn->prepare($sqlImages);
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->bind_result($id, $img);

        while($stmt->fetch()) {
            if ($_SESSION["user"] == $username) {
                $content .= "<form action='5c.php' method='POST'>
                <input type='hidden' name='id' value='$id'>
                <input type='hidden' name='username' value='$username'>
                <img src='images/$img'>
                <input type='submit' value='Delete'>
                </form>";
            } else {
                $content .= "<img src='images/$img'>";
            }
            $content .= "<br><br>";
        }

        // uploading images
        if($_SESSION["user"] == $username) {
            $content .= "<form action='5d.php' method='POST' enctype='multipart/form-data'>
            <input type='file' name='userfile' accept='image/*'>
            <input type='submit' value='Upload'>
            </form>";
        }

        echo $content;
    }

?>