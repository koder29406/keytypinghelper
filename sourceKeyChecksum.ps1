$input_file = "key"
$keylines = Get-Content -Path $input_file
$keyfile = Out-String -InputObject $keylines

Write-Output $keyfile

$sha_result = Get-FileHash -Algorithm SHA1 $input_file
$key_hash = $sha_result.Hash
$count = 0
Write-Output "   KEY HASH: $key_hash"

foreach ($line in $keylines) {
    $count++
    $stringAsStream = [System.IO.MemoryStream]::new()
    $writer = [System.IO.StreamWriter]::new($stringAsStream)
    $writer.write($line)
    $writer.Flush()
    $stringAsStream.Position = 0
    $sha_result = Get-FileHash -Algorithm SHA1 -InputStream $stringAsStream
    $line_hash = $sha_result.Hash
    Write-Output "LINE $count HASH: $line_hash"
}
