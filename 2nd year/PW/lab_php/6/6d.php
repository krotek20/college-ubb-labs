<?php

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "labphp";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if (isset($_POST["user"]) && isset($_POST["comment"]) && count($_POST) == 2) {
        $user = addslashes(htmlentities($_POST["user"], ENT_COMPAT, "UTF-8"));
        $comment = addslashes(htmlentities($_POST["comment"], ENT_COMPAT, "UTF-8"));

        if ($user == "" || strlen($username) > 255 || $comment == "" || strlen($comment) > 255) {
            header("Location: 6.html");
            exit();
        }

        $sql = "INSERT INTO comentarii (user, comment, state) VALUES (?, ?, 0)";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ss", $user, $comment);
        $stmt->execute();
        header("Location: 6b.php");
        exit();
    }

?>