// Hàm gửi yêu cầu POST đến /upload với FormData
async function uploadFile(formData) {
  try {
    const response = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    console.log("Upload Response:", data);
    return data;
  } catch (error) {
    console.error("Error uploading file:", error);
    throw error;
  }
}

// Hàm gửi yêu cầu GET đến /process_file
async function processFile() {
  try {
    const response = await fetch("http://127.0.0.1:5000/process_file");
    const data = await response.json();
    console.log("Process File Response:", data);
    return data;
  } catch (error) {
    console.error("Error processing file:", error);
    throw error;
  }
}

var formData = new FormData();
document
  .getElementById("fileInput")
  .addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
      formData.append("file", file);

      // Hiển thị tên tệp dưới nút "Import CSV"
      document.getElementById(
        "import-button"
      ).textContent = `Import: ${file.name}`;
    }
  });

document
  .getElementById("send-file-button")
  .addEventListener("click", async function (event) {
    try {
      const formData_ = await uploadFile(formData);
      console.log(formData_);
    } catch (error) {
      console.error("Error sending file:", error);
    }
  });

// Sự kiện khi nút "Hiển thị Biểu đồ" được nhấn
document
  .getElementById("show-visualization-button")
  .addEventListener("click", async function () {
    try {
      const data = await processFile();
      // Hiển thị kết quả từ Flask, có thể là biểu đồ hoặc dữ liệu
      document.getElementById("visualization-container").innerHTML = data.data;
    } catch (error) {
      console.error("Error showing visualization:", error);
      alert("Đã xảy ra lỗi khi xử lý tệp.");
    }
  });
