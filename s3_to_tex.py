import paramiko
import openai
import boto3
import subprocess
bucket_name = "young9-crawling"
s3 = boto3.resource("s3")
command = "aws s3 ls s3://young9-crawling/sm_test/"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
# 결과를 문자열로 변환하여 개행 문자('\n')로 분할하고 이를 리스트로 저장
output_lines = result.stdout.split('\n')
# 개행 문자('\n')로 분할된 결과에서 빈 문자열 제거
objects = list(filter(None, output_lines))
num = len(objects)
print(num)
client = openai.OpenAI(
        api_key=''
    )
for i in range(num):
    with open('sm_' + str(i) +'.txt', 'r') as file:
        text = file.read()
    #new_file = open("s" + str(i) + ".txt", "w")
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You summarizes the content in the text."},
            {"role": "user", "content": text + "를 요약해줘. 공지사항 제목, 신청 기간, 자격요건, 신청대상/선발대상, 구비서류/제출서류 항목별로. 한국어로해주고, 없는 내용 생성하거나 있는 내용 바꾸지 마"}
        ]
    )
    #new_file.write(completion.choices[0].message.content)
    file_name =  f"s{i}.txt"
    s3_path = "sm_openaigen/"+ file_name
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=completion.choices[0].message.content)
    print(completion.choices[0].message.content)