<?php
$pins = [12, 13, 16, 17, 18, 19, 20, 5, 7, 8,];
$pin_status = [];

foreach ($pins as $pin) {
    $status = trim(shell_exec("gpio -g read $pin"));
    $pin_status[$pin] = $status;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $action = $_POST['action'];

    if ($action == "on_all") {
        foreach ($pins as $pin) {
            $command_mode = "gpio -g mode $pin out";
            $command_write = "gpio -g write $pin 1";
            system($command_mode);
            system($command_write);
        }
    } elseif ($action == "off_all") {
        foreach ($pins as $pin) {
            $command_mode = "gpio -g mode $pin out";
            $command_write = "gpio -g write $pin 0";
            system($command_mode);
            system($command_write);
        }
    } elseif (isset($_POST['pin']) && isset($_POST['state'])) {
        $pin = $_POST['pin'];
        $state = $_POST['state'];
        if (in_array($pin, $pins)) {
            $command_mode = "gpio -g mode $pin out";
            $command_write = "gpio -g write $pin " . ($state == "on" ? "1" : "0");
            system($command_mode);
            system($command_write);
        }
    }

    // Refresh the page to update the toggle switch status
    header("Location: " . $_SERVER['PHP_SELF']);
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Kontrol Lampu IoT</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        .switch-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin: 20px 0;
        }
        .switch {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 10px;
            background: #fff;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .switch label {
            margin-bottom: 10px;
            font-weight: bold;
        }
        .toggle-switch {
            position: relative;
            display: inline-block;
            width: 60px;
            height: 34px;
        }
        .toggle-switch input {
            display: none;
        }
        .slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            transition: .4s;
            border-radius: 34px;
        }
        .slider:before {
            position: absolute;
            content: "";
            height: 26px;
            width: 26px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            transition: .4s;
            border-radius: 50%;
        }
        input:checked + .slider {
            background-color: #2196F3;
        }
        input:checked + .slider:before {
            transform: translateX(26px);
        }
        .control-buttons {
            margin-top: 20px;
        }
        .control-buttons button {
            margin: 5px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            color: white;
        }
        .on-button {
            background-color: #4CAF50;
        }
        .off-button {
            background-color: #f44336;
        }
    </style>
</head>
<body>
    <h1>Kontrol Lampu IoT</h1>
    <form method="post">
        <div class="switch-container">
            <?php
            foreach ($pins as $pin) {
                $checked = $pin_status[$pin] == "1" ? "checked" : "";
                echo "
                <div class='switch'>
                    <label for='lampu$pin'>Lampu $pin</label>
                    <label class='toggle-switch'>
                        <input type='checkbox' name='state' value='$pin' onchange='this.form.pin.value=$pin; this.form.state.value=this.checked ? \"on\" : \"off\"; this.form.submit();' $checked>
                        <span class='slider'></span>
                    </label>
                </div>
                ";
            }
            ?>
        </div>
        <input type="hidden" name="pin" value="">
        <input type="hidden" name="state" value="">
        <div class="control-buttons">
            <button type="submit" name="action" value="on_all" class="on-button">Hidupkan Semua Lampu</button>
            <button type="submit" name="action" value="off_all" class="off-button">Matikan Semua Lampu</button>
        </div>
    </form>
</body>
</html>
