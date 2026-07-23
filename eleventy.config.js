const prettier = require("prettier");

module.exports = async function(eleventyConfig) {
  const { HtmlBasePlugin } = await import("@11ty/eleventy");
  eleventyConfig.addPassthroughCopy("**/*.incl");
  eleventyConfig.addPassthroughCopy("**/*.css");
  eleventyConfig.addPassthroughCopy("favicon.ico");
  eleventyConfig.addPassthroughCopy("robots.txt");
  eleventyConfig.addPassthroughCopy("devmtg/**/*.{cc,css,dir,eot,eps,gz,htaccess,htc,incl,jpg,js,key,md,otf,pdf,php,png,PNG,ppsx,ppt,pptx,scale,scss,svg,tbz2,ttf,txt,woff,xml}");
  eleventyConfig.addPassthroughCopy("img");
  eleventyConfig.addPlugin(HtmlBasePlugin);
  eleventyConfig.addTransform("prettier", async function(content, outputPath) {
    if (outputPath && outputPath.endsWith(".html")) {
      try {
        return await prettier.format(content, {
          parser: "html",
        });
      } catch (error) {
        console.warn(`Prettier error on ${outputPath}: `, error);
        return content;
      }
    }
    return content;
  });
  return {
    markdownTemplateEngine: false,
    htmlTemplateEngine: false,
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      data: "_data"
    }
  };
};
