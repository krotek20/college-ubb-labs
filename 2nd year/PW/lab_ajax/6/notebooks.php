<?php 

    $criteria = $_GET["criteria"];
    $filterData = $_GET["data"]; 

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "labajax";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT manufacturer, model, ram, hdd, videocard FROM notebooks";
    if ($criteria != "none") {
        $sql .= " where " . $criteria . " like '%" . $filterData . "%';";
    }

    $statement = $conn->prepare($sql);
    $statement->execute();
    $statement->bind_result($manufacturer, $model, $ram, $hdd, $videocard);

    $notebooks = array();
    while ($statement->fetch()) {
        $notebook = new StdClass();
        
        //attributes
        $notebook->manufacturer = $manufacturer;
        $notebook->model = $model;
        $notebook->ram = $ram;
        $notebook->hdd = $hdd;
        $notebook->videocard = $videocard;

        array_push($notebooks, $notebook);
    }

    echo json_encode($notebooks);
    $statement->close();
    $conn->close();

?>