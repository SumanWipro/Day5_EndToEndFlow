pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
        APP_NAME = 'calculator'
        RELEASE_DIR = 'dist'
    }

    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {

        // ── Stage 1: Build ───────────────────────────────────────────────────
        // Set up the virtual environment, lint the code, and produce
        // a distributable wheel + sdist.
        stage('Build') {
            steps {
                echo "Building ${APP_NAME}..."

                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip -q
                    pip install -r requirements.txt -q
                '''

                sh '''
                    . ${VENV_DIR}/bin/activate
                    flake8 calculator/ main.py --max-line-length=100 --exclude=.venv
                '''

                sh '''
                    . ${VENV_DIR}/bin/activate
                    python -m build --outdir ${RELEASE_DIR}
                '''
            }

            post {
                success {
                    echo 'Build stage passed.'
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                }
                failure {
                    echo 'Build stage failed.'
                }
            }
        }

        // ── Stage 2: Test ────────────────────────────────────────────────────
        // Run the full test suite with coverage enforcement.
        // Pipeline fails if coverage drops below 60%.
        stage('Test') {
            steps {
                echo 'Running tests...'

                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest tests/ -v \
                        --cov=${APP_NAME} \
                        --cov-report=term-missing \
                        --cov-report=xml:coverage.xml \
                        --cov-fail-under=60
                '''
            }

            post {
                always {
                    junit allowEmptyResults: true, testResults: '**/test-results.xml'
                }
                success {
                    echo 'All tests passed.'
                }
                failure {
                    echo 'Tests failed.'
                }
            }
        }

        // ── Stage 3: Deploy ──────────────────────────────────────────────────
        // Runs only on the main branch after tests pass.
        // Copies the built artifact to the release directory.
        stage('Deploy') {
            when {
                branch 'main'
            }

            steps {
                echo "Deploying ${APP_NAME} v${BUILD_NUMBER}..."

                sh '''
                    mkdir -p release
                    cp ${RELEASE_DIR}/*.whl release/
                    cp ${RELEASE_DIR}/*.tar.gz release/
                    echo "Build ${BUILD_NUMBER} deployed at $(date)" > release/deploy.log
                '''
            }

            post {
                success {
                    archiveArtifacts artifacts: 'release/*', fingerprint: true
                    echo "Deployment complete: ${APP_NAME} build ${BUILD_NUMBER}"
                }
                failure {
                    echo 'Deployment failed.'
                }
            }
        }
    }

    // ── Post pipeline ────────────────────────────────────────────────────────
    post {
        always {
            cleanWs()
        }
        success {
            echo "Pipeline succeeded: ${APP_NAME} build ${BUILD_NUMBER}"
        }
        failure {
            echo "Pipeline failed: ${APP_NAME} build ${BUILD_NUMBER}"
        }
    }
}
