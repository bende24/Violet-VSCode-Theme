Write-Output "Hello, World!"

$x = 10
$y = 20
$sum = $x + $y
Write-Output "Sum: $sum"

$numbers = @(1, 2, 3)
foreach ($number in $numbers) {
    Write-Output "Number: $number"
}

# Functions and pipeline support
function Get-Square {
    param([int]$number)
    return $number * $number
}

$numbers | ForEach-Object { Get-Square $_ } | ForEach-Object { Write-Output "Square: $_" }

# Conditional statements
if ($x -eq 10) {
    Write-Output "x is 10"
} else {
    Write-Output "x is not 10"
}

# Working with files
$path = "output.txt"
"Hello, World!" | Out-File -FilePath $path
Write-Output "File written to $path"
