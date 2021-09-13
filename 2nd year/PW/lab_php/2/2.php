<?php

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "labphp";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $table = "<table>";
    $format = "
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>";
    $header = sprintf($format, "id", "nume", "prenume", "telefon", "email");
    $buttonURI = '2.php?offset=%d&limit=%d';

    if (isset($_GET["taskOption"])) {
        $option = addslashes(htmlentities($_GET["taskOption"], ENT_COMPAT, "UTF-8"));

        if(!is_numeric($option)) {
            header("Location: 2.html");
            exit();
        }

        $sql = "SELECT * FROM persoane LIMIT ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("i", $option);
        $stmt->execute();
        $stmt->bind_result($id, $nume, $prenume, $telefon, $email);

        while($stmt->fetch()) {
            $table .= sprintf($format, strval($id), $nume, $prenume, $telefon, $email);
        }
        $table .= "</table>";

        $prevButtonURI = sprintf($buttonURI, -$option, $option);
        $nextButtonURI = sprintf($buttonURI, $option, $option);

        echo $table . "<br><br><a href='$prevButtonURI'>Previous</a><br><a href='$nextButtonURI'>Next</a>";

        $stmt->close();
        $conn->close();
    } else if (isset($_GET["offset"]) && isset($_GET["limit"])) {
        $offset = addslashes(htmlentities($_GET["offset"], ENT_COMPAT, "UTF-8"));
        $limit = addslashes(htmlentities($_GET["limit"], ENT_COMPAT, "UTF-8"));

        if(!is_numeric($offset) || !is_numeric($limit)) {
            header("Location: 2.html");
            exit();
        }

        $sql = "SELECT * FROM persoane LIMIT ? OFFSET ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ii", $limit, $offset);
        $stmt->execute();
        $stmt->bind_result($id, $nume, $prenume, $telefon, $email);

        while($stmt->fetch()) {
            $table .= sprintf($format, strval($id), $nume, $prenume, $telefon, $email);
        }
        $table .= "</table>";

        $prevButtonURI = sprintf($buttonURI, $offset - $limit, $limit);
        $nextButtonURI = sprintf($buttonURI, $offset + $limit, $limit);

        echo $table . "<br><br><a href='$prevButtonURI'>Previous</a><br><a href='$nextButtonURI'>Next</a>";

        $stmt->close();
        $conn->close();
    }

?>