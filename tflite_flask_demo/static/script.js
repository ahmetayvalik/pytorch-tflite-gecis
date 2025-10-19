async function testPerformance() {
    document.getElementById("result").innerText = "Test yapılıyor...";
    const response = await fetch("/test");
    const data = await response.json();
    document.getElementById("result").innerText = `Çalışma süresi: ${data.time_ms} ms`;
}
