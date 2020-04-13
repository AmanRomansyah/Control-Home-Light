<?php
	system("gpio -g mode 12 out");
	system("gpio -g write 12 1");
	include "index.php"
?>
