<?php
	system("gpio -g mode 5 out");
	system("gpio -g write 5 1");
	include "index.php"
?>
