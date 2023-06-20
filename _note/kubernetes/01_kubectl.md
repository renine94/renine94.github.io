# Kubectl

## 클러스터내의 리소스에 포트포워딩하여 접근하기
> [공식문서](https://kubernetes.io/ko/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)

- pods 로 포트포워딩
```bash
kubectl port-forward pods/mongo-75f59d57f4-4nd6q 28015:27017
```

- deployment 로 포트포워딩
```bash
kubectl port-forward deployment/mongo 28015:27017
```

- replicaset 으로 포트포워딩
```bash
kubectl port-forward replicaset/mongo-75f59d57f4 28015:27017
```

- service 로 포트포워딩
```bash
kubectl port-forward service/<service-name> <local-port>:<remote-port>
```



## 모든 Pods 의 Log 보기
`kubectl logs -l app=quizium-backend -f --timestamps=true --max-log-requests 8`

- `-l` 라벨 이름
- `-f` 실시간으로 계속 보기
- `--max-log-requests` 동시에 받는 요청수(?)

