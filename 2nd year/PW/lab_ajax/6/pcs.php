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

    $sql = "SELECT manufacturer, procesor, ram, hdd FROM pcs";
    if ($criteria != "none") {
        $sql .= " where " . $criteria . " like '%" . $filterData . "%';";
    }
    $statement = $conn->prepare($sql);
    $statement->execute();
    $statement->bind_result($manufacturer, $procesor, $ram, $hdd);

    $pcs = array();
    while ($statement->fetch()) {
        $pc = new StdClass();
        
        //attributes
        $pc->manufacturer = $manufacturer;
        $pc->procesor = $procesor;
        $pc->ram = $ram;
        $pc->hdd = $hdd;

        array_push($pcs, $pc);
    }

    echo json_encode($pcs);
    $statement->close();
    $conn->close();

?>