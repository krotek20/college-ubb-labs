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

    $username = $_SESSION["user"];
    if ($username && strlen($username) <= 255) {
        $uploadfile = "images/" . $username . "_" . basename($_FILES['userfile']['name']);
        if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
            $filename = $username . "_" . $_FILES["userfile"]["name"];
            $sql = "INSERT INTO imagini (username, img) VALUES (?, ?)";
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("ss", $username, $filename);
            $stmt->execute();
        }
    }

    header("Location: 5b.php?user=$username");
    exit();

?>