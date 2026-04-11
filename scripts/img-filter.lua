-- img-filter.lua — 将 HTML <img> 标签转为 pandoc Image 元素
-- 这样 pandoc 转 docx 时能正确嵌入图片

function RawInline(el)
  if el.format == "html" then
    local src = el.text:match('src="([^"]+)"')
    if src then
      -- URL 解码文件名
      local decoded = src:gsub("%%(%x%x)", function(hex)
        return string.char(tonumber(hex, 16))
      end)
      return pandoc.Image("", decoded)
    end
  end
end

function RawBlock(el)
  if el.format == "html" then
    local src = el.text:match('src="([^"]+)"')
    if src then
      local decoded = src:gsub("%%(%x%x)", function(hex)
        return string.char(tonumber(hex, 16))
      end)
      return pandoc.Para({pandoc.Image("", decoded)})
    end
  end
end
