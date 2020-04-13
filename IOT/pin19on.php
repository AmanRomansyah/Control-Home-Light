<?php
	system("gpio -g mode 19 out");
	system("gpio -g write 19 1");
	include "index.php"
?>
