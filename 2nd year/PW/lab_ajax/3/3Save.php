<?php
    $idCerut = $_GET["id"];
    $numeCerut = $_GET["nume"];
    $prenumeCerut = $_GET["prenume"];
    $telefonCerut = $_GET["telefon"];
    $emailCerut = $_GET["email"];

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "labajax";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "UPDATE t2 SET nume = ?, prenume = ?, telefon = ?, email = ? WHERE id = ?";

    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ssssi",$numeCerut, $prenumeCerut, $telefonCerut, $emailCerut, $idCerut);
    $stmt->execute();

    $stmt->close();
    $conn->close();
?>