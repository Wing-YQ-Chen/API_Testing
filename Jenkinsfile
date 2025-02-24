pipeline {
	agent any
    stages {

		stage('Build') {
			steps {
				bat """
				echo "Building"
                python -m venv venv
                call venv\\Scripts\\activate
                pip list
                pip install -r requirements.txt -i "https://mirrors.aliyun.com/pypi/simple/"
                pip list
                """

            }
        }


		stage('Run Testing') {
			steps {
				bat """
				echo "Run Testing"
				python script\\main.py
				"""
			}
			post {
				always {
					archiveArtifacts artifacts: 'Reports/index.html', allowEmptyArchive: true
				}
			}
		}

    }
}
