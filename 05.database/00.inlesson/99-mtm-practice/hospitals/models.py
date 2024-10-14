from django.db import models

# 1
# class Doctor(models.Model):
#     name = models.TextField()

#     def __str__(self):
#         return f'{self.pk}번 의사 {self.name}'


# class Patient(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     name = models.TextField()

#     def __str__(self):
#         return f'{self.pk}번 환자 {self.name}'


# 2
# class Doctor(models.Model):
#     name = models.TextField()

#     def __str__(self):
#         return f'{self.pk}번 의사 {self.name}'


# # 외래키 삭제
# class Patient(models.Model):
#     name = models.TextField()

#     def __str__(self):
#         return f'{self.pk}번 환자 {self.name}'


# # 중개모델 작성
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'


# 3
# class Doctor(models.Model):
#     name = models.TextField()

#     def __str__(self):
#         return f'{self.pk}번 의사 {self.name}'


# class Patient(models.Model):
#     # ManyToManyField 작성
#     doctors = models.ManyToManyField(Doctor)
#     name = models.TextField()

#     def __str__(self):
#         return f'{self.pk}번 환자 {self.name}'

# 5
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
