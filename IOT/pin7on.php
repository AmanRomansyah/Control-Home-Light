<?php
	system("gpio -g mode 7 out");
	system("gpio -g write 7 1");
	include "index.php"
?>
