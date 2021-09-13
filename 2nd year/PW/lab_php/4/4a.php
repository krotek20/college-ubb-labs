<?php

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "labphp";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    function generateRandomString($length = 20) {
        return substr(str_shuffle(str_repeat($x='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
            ceil($length / strlen($x)))), 1, $length);
    }

    $confirmString = "http://localhost/lab_php/4/4b.php?key=%s";

    if (isset($_POST["username"]) && isset($_POST["password"]) && isset($_POST["email"])) {
        $username = addslashes(htmlentities($_POST["username"], ENT_COMPAT, "UTF-8"));
        $password = addslashes(htmlentities($_POST["password"], ENT_COMPAT, "UTF-8"));
        $email = addslashes(htmlentities($_POST["email"], ENT_COMPAT, "UTF-8"));

        if ($username == "" || $password == "" || strlen($username) > 255 || strlen($password) > 255 || strlen($email) > 255) {
            header("Location: 4.html");
            exit();
        }

        // login
        if ($email == "") {
            $sql = "SELECT * FROM utilizatori WHERE username = ? and password = ?";
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("ss", $username, $password);
            $stmt->execute();

            if ($stmt->fetch()) {
                echo "Successful authentication!";
            } else {
                echo "Authentication failed!";
            }

            $stmt->close();
            $conn->close();
        } 
        // register
        else {
            $to_email = $email;
            $key = generateRandomString();
            $subject = "Registration confirmation!";
            $message = sprintf($confirmString, $key);
            $headers = "From:sergentul2006@gmail.com";
            
            if (mail($to_email, $subject, $message, $headers)) {
                $sql = "INSERT INTO confirmari VALUES(?, ?, ?)";
                $stmt = $conn->prepare($sql);
                $stmt->bind_param("sss", $username, $password, $key);
                $stmt->execute();

                echo "Email successfully sent to $to_email";

                $stmt->close();
            } else {
                echo "Email sending failed...";
            }

            $conn->close();
        }
    }

?>