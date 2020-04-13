<?php
	include "index.php";
	system("gpio -g mode 17 out");
	system("gpio -g mode 17 out");
	
	system("gpio -g write 17 0");
	sleep(10);
	system("gpio -g write 17 1");
?>
