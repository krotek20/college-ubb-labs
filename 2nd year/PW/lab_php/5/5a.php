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

    if (isset($_POST["username"]) && isset($_POST["password"])) {
        $username = addslashes(htmlentities($_POST["username"], ENT_COMPAT, "UTF-8"));
        $password = addslashes(htmlentities($_POST["password"], ENT_COMPAT, "UTF-8"));

        if ($username == "" || $password == "" || strlen($username) > 255 || strlen($password) > 255) {
            header("Location: 5.html");
            exit();
        }

        $sql = "SELECT * FROM utilizatori WHERE username = ? AND password = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ss", $username, $password);
        $stmt->execute();
        if ($stmt->fetch()) {
            header("Location: 5b.php?user=$username");
            $_SESSION["user"] = $username;
        }
        else {
            header("Location: 5.html");
        }
        exit();
    }

?>