import subprocess
import json

def process_hwp(file_path, hwp_jar_path, work_dir):
    try:
        result = subprocess.run(
            ["python3", "hwpx_loader.py",
             "--hwpx_jar_path", hwp_jar_path,
             "--file_path", file_path],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        try:
            output = json.loads(result.stdout)
        except json.JSONDecodeError:
            return {"error": "JSON 디코딩 실패", "raw_output": result.stdout}

        if "error" in output:
            return {"error": f"HWPX extract failed: {output['error']}"}

        return {"text": output["text"]}

    except Exception as e:
        return {"error": f"Subprocess 실패: {str(e)}"}
