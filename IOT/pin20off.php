<?php
	system("gpio -g mode 20 out");
	system("gpio -g write 20 0");
	include "index.php"
?>
