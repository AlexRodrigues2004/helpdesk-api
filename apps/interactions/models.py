from django.db import models
from apps.users.models import User
from apps.tickets.models import Ticket


class Interaction(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='interactions',
        verbose_name='Chamado'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='interactions',
        verbose_name='Usuário'
    )
    message = models.TextField(verbose_name='Mensagem')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')

    class Meta:
        verbose_name = 'Interação'
        verbose_name_plural = 'Interações'
        ordering = ['created_at']

    def __str__(self):
        return f'Interação #{self.id} - Chamado #{self.ticket.id}'