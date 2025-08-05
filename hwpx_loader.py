import jpype
import argparse
import json

def hwpx_extract(hwpx_jar_path, file_path):
    jpype.startJVM(
        jpype.getDefaultJVMPath(),
        "-Djava.class.path={classpath}".format(classpath=hwpx_jar_path),
        convertStrings=True,
    )

    HWPXFile = jpype.JClass('kr.dogfoot.hwpxlib.reader.HWPXReader')
    TextExtractor = jpype.JClass('kr.dogfoot.hwpxlib.tool.textextractor.TextExtractor')
    TextExtractMethod = jpype.JClass('kr.dogfoot.hwpxlib.tool.textextractor.TextExtractMethod')
    TextMarks = jpype.JClass('kr.dogfoot.hwpxlib.tool.textextractor.TextMarks')

    hwpx_file = HWPXFile.fromFilepath(file_path)
    text_extract_method = TextExtractMethod.AppendControlTextAfterParagraphText
    text_marks = TextMarks()

    hwpxtext = TextExtractor.extract(hwpx_file, text_extract_method, True, text_marks)
    return hwpxtext

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Hwpx loader')
    parser.add_argument('--hwpx_jar_path', type=str, required=True)
    parser.add_argument('--file_path', type=str, required=True)
    args = parser.parse_args()

    try:
        text = hwpx_extract(args.hwpx_jar_path, args.file_path)
        print(json.dumps({"text": text}, ensure_ascii=False))   # 실제 출력 내용 
    except Exception as e:
        print(json.dumps({"error": str(e)}))  # 예외 처리
