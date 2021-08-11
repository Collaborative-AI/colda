module.exports = {
    configureWebpack: config => {
      if (process.env.NODE_ENV === 'production') {
        // mutate config for production...
        console.log("vvvv")
      } else {
        // mutate for development...

        console.log("zzzz")
      }
    }
  }