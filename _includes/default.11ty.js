module.exports = function(data) {
  const stem = data.page.filePathStem || "";
  const parts = stem.split("/").filter(p => p !== "");
  const depth = Math.max(0, parts.length - 1);
  const prefix = depth === 0 ? "" : "../".repeat(depth);

  return `<!--#include virtual="${prefix}header.incl" -->\n` + data.content + `<!--#include virtual="${prefix}footer.incl" -->\n`;
};
