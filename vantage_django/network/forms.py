from django import forms

PROTO_CHOICES = [("", "Any"), ("TCP", "TCP"), ("UDP", "UDP"), ("ICMP", "ICMP")]

class FilterForm(forms.Form):
    src_ip = forms.CharField(
        required=False,
        label="Source IP",
        widget=forms.TextInput(attrs={"placeholder": "e.g. 10.0.0"})
    )
    dst_ip = forms.CharField(
        required=False,
        label="Destination IP",
        widget=forms.TextInput(attrs={"placeholder": "e.g. 192.168.1."})
    )
    proto = forms.ChoiceField(
        choices=PROTO_CHOICES,
        required=False,
        label="Protocol",
        help_text=""
    )
    min_port = forms.IntegerField(
        required=False, min_value=0, max_value=65535,
        label="Min Dst port",
        widget=forms.NumberInput(attrs={"placeholder": "e.g. 1"})
    )
    max_port = forms.IntegerField(
        required=False, min_value=0, max_value=65535,
        label="Max Dst port",
        widget=forms.NumberInput(attrs={"placeholder": "e.g. 65535"})
    )
