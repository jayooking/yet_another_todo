def buildApp(){
    echo "building the application"
    sh "docker build -t another-todo-app ."
}

def testApp(){
    echo "testing the apply"
}

def deployApp(){
    echo "deploying the app"
}

return this