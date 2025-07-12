# Projeto Final - Fundamentos de DevOps

Este projeto consiste na criação de um ambiente automatizado usando Vagrant, Ansible, Kubernetes (Kind) e ArgoCD para deploy de uma aplicação FastAPI + PostgreSQL (backend) e um frontend estático em Nginx.

## Tecnologias Utilizadas

* Vagrant + VirtualBox
* Ansible
* Docker
* Kind (Kubernetes in Docker)
* kubectl
* ArgoCD
* FastAPI (Backend)
* PostgreSQL (Banco de dados)
* Nginx (Frontend)

## Estrutura do Projeto

```
projeto-devops/
├── Vagrantfile
├── playbook.yml
├── app/                  # FastAPI app
├── frontend/             # HTML + JS estático
├── k8s/                  # Manifests Kubernetes
│   ├── backend.yaml
│   ├── frontend.yaml
│   └── postgres.yaml
```

## Etapas do Projeto

### 1. Provisionamento da VM

Utilizando o Vagrant para subir a VM e o Ansible para provisionar:

```bash
vagrant up
```

### 2. Instalação das ferramentas

Instalação automatizada do Docker, Kind e kubectl pela role Ansible.

### 3. Criação do Cluster Kubernetes

Dentro da VM:

```bash
kind create cluster --config kind-config.yaml
```

### 4. Instalação do ArgoCD

```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### 5. Deploy via GitOps (ArgoCD)

* A aplicação foi configurada no ArgoCD apontando para o repositório:
  [https://github.com/kauaDev22/prova-final-devops](https://github.com/kauaDev22/prova-final-devops)

### 6. Aplicativos no Ar

#### Backend (FastAPI + PostgreSQL)

* Porta exposta via `NodePort`
* Porta 8000 redirecionada com:

```bash
kubectl port-forward svc/fastapi-service --address 0.0.0.0 8000:8000
```

#### Frontend (Nginx)

* HTML estático renderizado via imagem Docker customizada
* Redirecionado com:

```bash
kubectl port-forward svc/frontend-service --address 0.0.0.0 30001:80
```

#### ArgoCD (Interface Web)

```bash
kubectl port-forward svc/argocd-server -n argocd --address 0.0.0.0 8080:443
```

## Considerações

* O repositório Git serve como fonte de verdade (GitOps)
* Todos os serviços estão acessíveis a partir do IP da VM pela máquina host
* Foram criados services do tipo `NodePort` para facilitar o acesso externo

---

## Autor

Kauã Jotta - @kauaDev22

[Repositório no GitHub](https://github.com/kauaDev22/prova-final-devops)

---

## Tutorial de Uso (Rodar Projeto na Sua Máquina)

### Pré-requisitos

* VirtualBox
* Vagrant
* Git

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/kauaDev22/prova-final-devops.git
cd prova-final-devops
```

2. Suba a VM e aguarde a configuração automatizada:

```bash
vagrant up
```

3. Acesse a VM:

```bash
vagrant ssh
```

4. Crie o cluster Kubernetes:

```bash
kind create cluster --config kind-config.yaml
```

5. Aguarde o ArgoCD aplicar os manifests automaticamente.

6. Faça os redirecionamentos de porta:

```bash
kubectl port-forward svc/fastapi-service --address 0.0.0.0 8000:8000 &
kubectl port-forward svc/frontend-service --address 0.0.0.0 30001:80 &
kubectl port-forward svc/argocd-server -n argocd --address 0.0.0.0 8080:443 &
```

7. Acesse os serviços no navegador:

* Frontend: [http://192.168.56.10:30001](http://192.168.56.10:30001)
* Backend: [http://192.168.56.10:8000](http://192.168.56.10:8000)
* ArgoCD: [https://192.168.56.10:8080](https://192.168.56.10:8080)
