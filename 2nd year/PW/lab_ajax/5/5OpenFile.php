<?php 
	$file = $_GET["file"];
	echo "<div id=\"file\"";
	$fh = fopen($file, 'r');
    $pageText = fread($fh, 25000);
    echo nl2br($pageText);
	echo "</div>";
 ?>