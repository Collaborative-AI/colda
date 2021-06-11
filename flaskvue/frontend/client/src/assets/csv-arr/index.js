import jschardet from 'jschardet'
import Papa from 'papaparse'

/**
 * csv file to 2D arr
 * */
// 检查编码，引用了 jschardet
function checkEncoding(base64Str) {
  // 这种方式得到的是一种二进制串
  var str = atob(base64Str.split(';base64,')[1])
  // console.log(str);
  // 要用二进制格式
  var encoding = jschardet.detect(str)
  encoding = encoding.encoding
  // console.log( encoding );
  if (encoding === 'windows-1252') {	// 有时会识别错误（如UTF8的中文二字）
    encoding = 'ANSI'
  }
  return encoding
}
function csv(file) {
  return new Promise((resolve, reject) => {
  // let file = this.$refs.csvData.files[0]
    const fReader = new FileReader()
    fReader.readAsDataURL(file)
    fReader.onload = function(evt) {
      const data = evt.target.result
      // console.log( data );
      const encoding = checkEncoding(data)
      // console.log(encoding);
      // 转换成二维数组，需要引入Papaparse.js
      Papa.parse(file, {
        encoding: encoding,
        complete: function(results) {		// UTF8 \r\n与\n混用时有可能会出问题
          // console.log(results)
          const res = results.data
          if (res[ res.length - 1 ] === '') {	// 去除最后的空行
            res.pop()
          }
          resolve(res)
        }
      })
    }
  })
}
export default {
  csv
}
